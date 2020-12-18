function check_num_files() {
    var f_num = document.getElementById("id_files").files.length;
    if (f_num > 10){
        document.getElementById('send').disabled = true;
        document.getElementById('alert').style.display = "flex";
    }
    if (f_num < 10){
        document.getElementById('send').disabled = false;
        document.getElementById('alert').style.display = "none";
    }
}