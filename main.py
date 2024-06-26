import os

def file_writer(data, letter, output_dir):
    filename = os.path.join(output_dir, f"{letter.lower()}.txt")
    with open(filename, "a") as file:
        file.write(data)
    print(f"{letter.upper()} processed!")

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
    output_dir = os.path.join("results")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open('words.txt', 'r') as file:
        for data in file:
            letter = data[:2]
            file_writer(data, letter, output_dir)

    result_maker(output_dir)
    os.rmdir(output_dir)


if __name__ == '__main__':
    main()
