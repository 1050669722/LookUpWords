@REM conda create --name LookUpWordsInstallationEnv --file environment.yml -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
@REM conda activate LookUpWordsInstallationEnv

@REM pyinstaller -F main.py --noconsole -n ProcessStringFromYoudaoDict
pyinstaller -F main.py -n LookUpWords