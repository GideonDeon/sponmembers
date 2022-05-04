let username = "NationalcommandeR";
let password = "seCure101";
let user = document.form.username
let pass = document.getElementById('pass')

function validate(){
    if(user.value.match(username)){
      
    }
    else{
        alert('Wrong username!')
        return false
    }

    if(pass.value.match(password)){
       
    }
    else{
        alert('wrong password!')
        return false
    }
}
function tickall(tck){
    tck.checked = false
}

let stus = document.getElementById('status')

// function stat(){
//     stus.style.color="red"
// }stat()