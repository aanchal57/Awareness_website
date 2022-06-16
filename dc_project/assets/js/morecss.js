
    function moreless(p){
        var dots=document.getElementById("id-dots"+p);
        var hidetxt=document.getElementById("id-moretext"+p);
        var btn=document.getElementById("id-btn"+p);
        if (dots.style.display==="none"){
            dots.style.display="inline";
            hidetxt.style.display="none";
            btn.innerHTML="Read More";
        }
        else {
            dots.style.display="none";
            hidetxt.style.display="inline";
            btn.innerHTML="Read Less";
            
        }

    }
