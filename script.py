import subprocess

from misc import *
from data import Defaults

def start_script(builds: str, license: str, script: str) -> tuple:
    """Starts the default script."""
    printf("Starting the script...")    
    printf("Use an appropriate flag to set a new value for each default one: ")
    printf(f"Default path to a builds folder: {builds}")
    printf(f"Default path to a licence file: {license}")
    printf(f"Default path to a script file: {script}")
    if builds == Defaults.BUILDS:
        printf("Getting a list of folders...")    
        printf("Note that there can be several builds in the folder.")
        printf("The list of the builds in the folder is given below: ")
        for build in os.listdir(builds):
            printf(build)
        printf("Script execution can take several minutes")
        printf("Type a build number to process, e.g. 30251.")
    else:
        printf("Script execution can take several minutes")
        printf("Press Enter to continue...")
    printf("Type 'exit' to close the script.")    
    build_number = get_build_number(store_exit_values())    
    build_path = get_folder_path(build_number, builds)
    printf(f"The build folder path: {build_path}")
    printf("Check whether the folder is empty...")    
    env = set_env(f"{build_path}\\Bin64\\nodejs", license, f"{build_path}\\SourceData")
    command = f"{script}"
    return build_path, command, env


def script_start(build_path, command, env):
    """Starts the main script."""
    import shutil
    import tempfile
    temp_backup = tempfile.mkdtemp()
    temp_pdf_path = os.path.join(temp_backup, "pdf")
    shutil.move(f"{build_path}\\SourceData\\www\\help\\pdf", temp_pdf_path)
    subprocess.run(
        command,
        env=env,
        shell=True, 
        check=False
        )
    shutil.move(temp_pdf_path, f"{build_path}\\SourceData\\www\\help\\pdf")
    shutil.rmtree(temp_backup)
