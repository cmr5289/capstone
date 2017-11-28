
$("#bookToggle").click(function(){
    if($("#bookToggle").text()=="Hide Books"){
        $("#bookToggle").text("Show Books")
        $(".book_item").css("display","none")
    }
    else{
        $("#bookToggle").text("Hide Books")
        $(".book_item").css("display","block")   
    }    
})

$("#dvdToggle").click(function(){
    if($("#dvdToggle").text()=="Hide DVDs"){
        $("#dvdToggle").text("Show Books")
        $(".dvd_item").css("display","none")
    }
    else{
        $("#dvdToggle").text("Hide DVDs")
        $(".dvd_item").css("display","block")   
    }    
})