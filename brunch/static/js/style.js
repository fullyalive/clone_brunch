function showOrHide(){
    const sidebar = document.getElementById("sidebar");
    if(sidebar.style.display === "none"){
        if(screen.width <= 500){
            sidebar.style.width = "50%";
        }
        else if(screen.width <= 800){
            sidebar.style.width = "40%";
        }
        sidebar.style.display = "block";
    }
    else{
        sidebar.style.display = "none";
    }
}