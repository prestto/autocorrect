#! /bin/bash
function run_dev_server {
    
    # echo "starting environment"
    # pipenv shell

    # echo "installing packages..."
    # pipenv install

    echo "making migrations..."
    python manage.py makemigrations

    echo "migrating..."
    python manage.py migrate

    echo "runnning server"
    python manage.py runserver 0.0.0.0:8000
}

function help {
    echo "--help    :    list all pssible args"
    echo "dev       :    run a dev server"
}

echo $1
echo $( expr "$1" == ""  )


if [ "$1" = "" ]; then
    echo "please supply an argument, run with --help for options"
    exit 1
fi

case $1 in

    "dev")
        run_dev_server
        ;;

    "--help")
        echo "list of available args:"
        ;;

esac