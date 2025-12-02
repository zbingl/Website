    
let openLid = `
<pre>
   +--------------+
   |.------------.|
   ||            ||
   ||  <b>Welcome!</b>  ||
   ||            ||
   ||            ||
   |+------------+|
   +-..--------..-+
   .--------------.
  / /============\\ \\
 / /==============\\ \\
/____________________\\
\\____________________/
</pre>`;

let closedLid = `
<pre>







  
   .--------------.
  /                \\
 /__________________\\
/____________________\\
\\____________________/
</pre>`;

document.getElementById("asciiComputer").innerHTML = openLid;
let open = true;

function computerButtonChange() {
    const elem = document.getElementById("asciiComputer");
    elem.innerHTML = open ? closedLid : openLid;
    open = !open;
}
