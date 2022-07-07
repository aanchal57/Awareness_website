
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
    function showmore(p){
        var dots=document.getElementById("sub-head"+p);
        var hidetxt=document.getElementById("sub-text-more"+p);
        var btn=document.getElementById("id-read"+p);
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
    function cardmore(p){
        
        var hidetxt=document.getElementById("more-card"+p);
        var btn=document.getElementById("card-btn"+p);
        if (btn.innerHTML==="Read More"){
            
            hidetxt.style.display="inline";
            btn.innerHTML="Read Less";
        }
        else {
           
            hidetxt.style.display="none";
            btn.innerHTML="Read More";
            
        }

    }

    
    