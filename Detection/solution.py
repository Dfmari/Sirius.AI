from ultralytics import YOLO
import os
import csv


model = YOLO('model.pt')
#activation of the trained model using provided weights. 
results = model(source='Input', show=False, conf=0.5, save_txt=True, imgsz=(2101, 2101))

#Formatting of model output-----------------------------------------------------------------------------------------------------------------------------------------------------
Output = 'runs/detect/predict2/labels'
Input = 'Input'
def add_prefix(directory, prefix):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
            
            with open(filepath, 'w') as file:
                for line in lines:
                    file.write(prefix + line)

def replace1(file_path, find, replace):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        updated_line = line.replace(find, replace)
        updated_lines.append(updated_line)

    with open(file_path, 'w') as file:
        file.write(''.join(updated_lines))

def replace_all(directory, find, replace):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            replace1(file_path, find, replace)

def multiply(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the contents of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Process and modify the data
            modified_lines = []
            for line in lines:
                # Parse the CSV format
                data = line.strip().split(',')
            
                # Divide the numbers in all columns except the first one by 2101
                modified_data = [data[0]] + [str(int(float(value) * 2101)) for value in data[1:]]
            
                # Join the modified data back into a CSV format line
                modified_line = ','.join(modified_data) + '\n'
            
                modified_lines.append(modified_line)

        # Save the modified data back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)


def convert(directory, prefix_add, replace_empty, replace_comma, replace_num, replace_space):
    add_prefix(directory, prefix_add)
    replace_all(directory, replace_space, replace_comma)
    multiply(directory)
    replace_all(directory, replace_num, replace_empty)


convert(Output, 'Class_', '', ',', '.0', ' ')
