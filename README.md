# HTMLList-tag-script
To use this script, you want to use the command line via bash/terminal. 
The format of the command line argument is as follows:
	"python3 listitemscript.py test.txt "tag" "toAdd" "delim1, delim2, ..." output.txt"
<*> is the tag you want to add a tag after, so replacing tag with <li> would add "<toAdd>"" in front of the tag. so if I read file:

<li>object1</li>
<li>object2</li> 

The script outputs to output.txt:

<li><toAdd>object1</toAdd></li>
<li><toAdd>object2</toAdd></li>
