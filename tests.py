from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file

def main():
    wr_dr = "calculator"
    # root_contents = get_files_info(wr_dr)
    # print(root_contents)
    # pkg_contents = get_files_info(wr_dr, "pkg")
    # print(pkg_contents)
    # pkg_contents_1 = get_files_info(wr_dr, "/bin")
    # print(pkg_contents_1)
    # pkg_contents_2 = get_files_info(wr_dr, "../")
    # print(pkg_contents_2)

    # file content testing
    # print(get_file_content(wr_dr, "main.py"))
    # print(get_file_content(wr_dr, "pkg/calculator.py"))
    # print(get_file_content(wr_dr, "/bin/cat"))
    # print(get_file_content(wr_dr, "pkg/does_not_exist.py"))

    # file write testing
    # print(write_file(wr_dr, "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file(wr_dr, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file(wr_dr, "/tmp/temp.txt", "this should not be allowed"))
    # print(write_file(wr_dr, "pkg2/temp.txt", "this should be allowed"))

    # run python file testing
    print(run_python_file(wr_dr, "main.py"))
    print(run_python_file(wr_dr,"main.py",["3 + 5"]))
    print(run_python_file(wr_dr, "tests.py"))
    print(run_python_file(wr_dr, "../main.py"))
    print(run_python_file(wr_dr, "nonexistent.py"))
    print(run_python_file(wr_dr, "lorem.txt"))
main()