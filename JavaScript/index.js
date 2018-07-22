var request = new XMLHttpRequest();
request.onreadystatechange = function(){
    if(request.readyState === 4){
        if(request.status === 200){
            
        } else {

        }
    }

}
request.open("GET", "/api/cat");
request.send();