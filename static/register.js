let password = document.getElementById("password");
let confirmPassword = document.getElementById("confirm_password");
let errorText = document.getElementById("error_message");

function validatePassword(){
    if(password.value!==confirmPassword.value){
        errorText.textContent="*Password do not match!";
        errorText.style.color="red";
        return false;
    }
    else{
        errorText.textContent = "";
        return true;
    }
}
