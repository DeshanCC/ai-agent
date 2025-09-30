from functions.get_files_info import get_files_info

def main():
    wr_dr = "calculator"
    root_contents = get_files_info(wr_dr)
    print(root_contents)
    pkg_contents = get_files_info(wr_dr, "pkg")
    print(pkg_contents)
    pkg_contents_1 = get_files_info(wr_dr, "/bin")
    print(pkg_contents_1)
    pkg_contents_2 = get_files_info(wr_dr, "../")
    print(pkg_contents_2)

main()