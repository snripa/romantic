var user_input = 0//Initiate global variable
var checksum = 0

main()
function random_integers ()
{
  
    var first_integer =  Math.floor( Math.random() * (1000 - 100 + 1) ) + 100;//expression for taking random integers taken from
                                                                            //http://www.cyberguru.ru/web/html/javascript-samples-page15.html 
    var second_integer = Math.floor( Math.random() * (1000 - 100 + 1) ) + 100;
    return [first_integer, second_integer]
}

function forming_checksum (first_integer, second_integer)
{
    return first_integer+second_integer
}

function main(){
    //algorithm here
    var integers = []
    integers = random_integers ()
    var first = integers[0]
    var second = integers[1]
    document.getElementById("first").innerHTML = first;
    document.getElementById("second").innerHTML = second;
    checksum = forming_checksum(first, second)

}

function checking(cheksum, user_input)
{
    if (cheksum ==user_input){
        document.getElementById("request").className = "btn btn-lg btn-primary btn-block btn-signin";
        document.getElementById("captcha").className = "hidden";
    }
    else{
        main()//enter recursion, untill user answer corretly
    }
}

function GetResults (form) {
    user_input = form.inputbox.value;
    
    checking(checksum, user_input)
    
}