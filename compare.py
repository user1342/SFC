import argparse
import os
import filecmp

def compare_folders(source, target):
    """
    Compare the contents of two folders.

    Args:
        source (str): Path to the source folder.
        target (str): Path to the target folder.

    Returns:
        Dircmp: Object containing the comparison results.
    """
    diffs = filecmp.dircmp(source, target)
    return diffs

def compare_files(source_file, target_file):
    """
    Compare the content of two text files.

    Args:
        source_file (str): Path to the source file.
        target_file (str): Path to the target file.

    Returns:
        bool: True if the content of both files is identical, False otherwise.
    """
    with open(source_file, 'r', encoding='utf-8', errors='ignore') as sf, open(target_file, 'r', encoding='utf-8', errors='ignore') as tf:
        source_content = sf.read()
        target_content = tf.read()
    return source_content == target_content

def generate_txt_report(diffs, report_file):
    """
    Generate a TXT report based on the comparison results.

    Args:
        diffs (Dircmp): Object containing the comparison results.
        report_file (str): Path to the output TXT report file.
    """
    def format_txt(diff, path=""):
        output = ""
        for name in diff.common_dirs:
            output += format_txt(diff.subdirs[name], os.path.join(path, name))
        for name in diff.common_files:
            source_file = os.path.join(diff.left, name)
            target_file = os.path.join(diff.right, name)
            if not compare_files(source_file, target_file):
                output += f"Modified: {os.path.join(path, name)}\n"
        for name in diff.left_only:
            output += f"Removed: {os.path.join(path, name)}\n"
        for name in diff.right_only:
            output += f"Added: {os.path.join(path, name)}\n"
        return output

    report_content = format_txt(diffs)
    with open(report_file, 'w') as f:
        f.write(report_content)

def main():
    parser = argparse.ArgumentParser(description='Simple Folder Compare Tool')
    parser.add_argument('source', help='Path to the source folder')
    parser.add_argument('target', help='Path to the target folder')
    parser.add_argument('-o', '--output', default='comparison_report.txt', help='Output TXT report file')
    args = parser.parse_args()

    source = args.source
    target = args.target
    report_file = args.output

    if not os.path.exists(source) or not os.path.exists(target):
        print("Error: Source or target folder does not exist.")
        return

    print("Comparing folders...")
    diffs = compare_folders(source, target)
    print("Generating TXT report...")
    generate_txt_report(diffs, report_file)
    print(f"Comparison report generated at {report_file}")

if __name__ == "__main__":
    main()
