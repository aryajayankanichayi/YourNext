document.querySelector('.submit').onclick = function() {
    const pwd = document.querySelector('#pwd').value;
    const cpwd = document.querySelector('#cpwd').value;
    if(pwd !== cpwd) {
    alert("Incorrect password");
    } else {
    alert("Submitted succesfully");
    }
    
};
