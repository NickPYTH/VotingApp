//-------------------- Замена приветствия в зависимости от врмени дня
var current_time = new Date().getHours();
var welcome_msg = document.getElementById('welcome');
if (current_time >= 4 && current_time <= 11 )  welcome.textContent = "Доброе утро,";
else if (current_time > 11 && current_time <= 17 )  welcome.textContent = "Добрый день,";
else if (current_time > 17 && current_time <= 22 )  welcome.textContent = "Добрый вечер,";
else if (current_time > 22 && current_time < 4 )  welcome.textContent = "Доброго времени суток,";
//--------------------

//-------------------- Замена стиля у текста, у логотипа
document.getElementById("logo_text").style.color = "white";
document.getElementById("logo_text").style.marginLeft = "10px";
document.getElementById("branding").style.display = "flex";
document.getElementById("branding").style.alignItems = "center";
//--------------------

//-------------------- Замена стиля у текста подзаголовка в зависимости от страницы
if (window.location.pathname == "/admin/") document.getElementById("pretitle").style.display = "none";  // /admin/

//--------------------
