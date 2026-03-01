const openLid = `
<pre>
   +--------------+
   |.------------.|
   ||            ||
   ||  <b>Welcome!</b>  ||
   || (click me) ||
   ||            ||
   |+------------+|
   +-..--------..-+
   .--------------.
  / /============\\ \\
 / /==============\\ \\
/____________________\\
\\____________________/
</pre>`;

const closedLid = `
<pre>







  
   .--------------.
  /                \\
 /__________________\\
/____________________\\
\\____________________/
</pre>`;

document.getElementById("asciiComputer")!.innerHTML = openLid;

let isOpen = true;

function _computerButtonChange() {
  const elem = document.getElementById("asciiComputer");
  if (!elem) return;
  elem.innerHTML = isOpen ? closedLid : openLid;
  isOpen = !isOpen;
}
