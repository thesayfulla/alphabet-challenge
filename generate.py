import os
import random
import string
from multiprocessing import Process, Queue

size_in_gb = 1
size_in_bytes = size_in_gb * 1024 * 1024 * 1024


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters, k=length))


def write_random_strings(
    file_path: str, chunk_size, start_index, end_index, result_queue
):
    with open(file_path, "r+b") as f:
        f.seek(start_index)
        while f.tell() < end_index:
            f.write(generate_random_string(chunk_size).encode() + b"\n")
        result_queue.put(True)


def create_random_string_file(file_path: str):
    target_word_length = 20
    num_processes = os.cpu_count()

    with open(file_path, "wb") as f:
        f.seek(size_in_bytes - 1)
        f.write(b"\0")

    result_queue = Queue()

    processes = []
    chunk_start = 0
    chunk_end = size_in_bytes // num_processes

    for _ in range(num_processes):
        p = Process(
            target=write_random_strings,
            args=(file_path, target_word_length, chunk_start, chunk_end, result_queue),
        )
        processes.append(p)
        p.start()
        chunk_start = chunk_end
        chunk_end += size_in_bytes // num_processes

    for p in processes:
        p.join()

    print("File created.")


if __name__ == "__main__":
    create_random_string_file("/app/words.txt")
