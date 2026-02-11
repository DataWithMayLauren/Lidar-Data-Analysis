import csv

def analyze_lidar_frame(file_path):
    print(f"--- DataWithMayLauren Lidar Processor ---")
    print(f"Reading: {file_path}\n")
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            # We treat the text from the file as numbers (float)
            dist = (float(row['x'])**2 + float(row['y'])**2)**0.5
            print(f"Object {row['object_id']} ({row['class']}) is {dist:.2f} meters away.")
            count += 1
            
    print(f"\nTotal objects processed in this sequence: {count}")

if __name__ == "__main__":
    analyze_lidar_frame('kitti_sample.csv')
