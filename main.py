import os
from shutil import rmtree
from multiprocessing import cpu_count, Process, Queue

def worker(queue, output_dir):
    while True:
        data = queue.get()
        if data is None:
            break
        letter, text = data
        filename = os.path.join(output_dir, f"{letter.lower()}.txt")
        with open(filename, "a") as file:
            file.write(text)
        print(f"{letter.upper()} processed!")

def file_writer(data_queue, output_dir):
    num_workers = cpu_count()
    processes = []

    for _ in range(num_workers):
        p = Process(target=worker, args=(data_queue, output_dir))
        p.start()
        processes.append(p)

    return processes

def result_maker(output_dir):
    for root, _, files in os.walk(output_dir):
        for txt_file in sorted(files):
            file_path = os.path.join(root, txt_file)
            with open(file_path, "r") as file:
                content = sorted(file.readlines())
                with open('result.txt', 'a') as result:
                    for word in content:
                        result.write(word)

def main():
    output_dir = "results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data_queue = Queue(maxsize=6)
    processes = file_writer(data_queue, output_dir)

    with open('words.txt', 'r') as file:
        for data in file:
            letter = data[:2]
            data_queue.put((letter, data))

    for _ in processes:
        data_queue.put(None)

    for p in processes:
        p.join()

    result_maker(output_dir)
    
    rmtree(output_dir)

if __name__ == '__main__':
    main()
