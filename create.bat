@echo off

rem Automatizacion Iniciar Proyecto en GitHub - Diego Fagundez

:: Para que este script funcione debe leer la documentacion o usar sentido comun ya que es basico.
:: Llamo la funcion 
call :create %~1

cd
python create.py %~1
cd C:/Users/Home/Documents/project/%~1
type nul > README.md
git init
git remote add origin https://github.com/username/%~1.git
git add .
git commit -m "Commit Inicial"
git push -u origin master
code .

:: Finaliza la funcion
goto :fin

:: Defino la funcion create
:create
set var=%~1