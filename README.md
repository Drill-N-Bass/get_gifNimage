Function **get_gifNimage()** opens any image listed below:
* `jpg`
* `jpeg`
* `png`
* `svg`

Also it opens `gif` from a link (*in string format*). 
After that, it will be saved in the current folder, convert (if needed) to `png` (from `svg` format) and - finally - displayed. 
The function deletes the svg file after conversion - in that case, it will leave only the `png` version so there won't be any useless files in the folder.

**Importing and calling:**
```
import get_gifNimage
from get_gifNimage import get_gifNimage
# or, you can write:
# from get_gifNimage import *

# Then you can call the module (for ex.):
get_gifNimage('https://st2.depositphotos.com/1004199/6231/i/600/depositphotos_62310947-stock-photo-boxer-dog-on-white-background.jpg')
get_gifNimage('https://media.giphy.com/media/W80Y9y1XwiL84/giphy.gif')

# or:

import get_gifNimage

# Then you can call the module (for ex.):
get_gifNimage.get_gifNimage('https://st2.depositphotos.com/1004199/6231/i/600/depositphotos_62310947-stock-photo-boxer-dog-on-white-background.jpg')
get_gifNimage.get_gifNimage('https://media.giphy.com/media/W80Y9y1XwiL84/giphy.gif')
```
##### get_gifNimage(link, file_name_show=False, dict_appearance=False, show_error_logs=False, only_picture_name=False)

>**Parametrs:	link : string**
> - Quoted link.

>**menu**
> - Show all arguments and their description.

>**more_info**
> - show details about arguments function.

> **file_name_show : bool, default False**
> - If true, it shows the picture/gif and the file name below the picture output.

> **dict_appearance : bool, default False**
> - If true it will build a dictionary related to downloaded pictures/gifs in a separate file (json format). 
It will store data that will archive every use of our 'get_gifNimage' function.
It will be open and checked every time the main function : get_gifNimage - will be called.
It's needed when a link doesn't have a unique file name in the page path.

    An example of this situation is when we try to use get_gifNimage on this site:

        https://media.giphy.com

    Every gif here has the same name. Two different gifs below:

        https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif
        https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif

    Every time we call our main fuction 'get_gifNimage' (let's suppose we call it twice,
    for those links above), 
    the names for files in current folder will be:

        https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif -> file_name -> 'giphy.gif'
        https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif -> file_name -> 'giphy (1).gif'

    BUT, our 'file_name' + 'image_type_index_dot' object will see each link as:

        https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif -> 'file_name' + 'image_type_index_dot' = 'giphy.gif'
        https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif ->'file_name' + 'image_type_index_dot' = 'giphy.gif'

    Python record both, but it will rename second as: 'giphy (1).gif; in current folder.
    The problem is: our code detects name as 'giphy.gif' in link every time.
    We need to fix it, so the relation between 'file_name' object and links will be with logic:

        https://media.giphy.com/media/q1MeAPDDMb43K/giphy.gif -> 'file_name' + 'image_type_index_dot' = 'giphy.gif'
        https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif -> 'file_name' + 'image_type_index_dot' = 'giphy (1).gif'

> **show_error_logs : bool, default False**
> - If True it shows all errors passed by exception function.

> **only_picture_name : bool, default False**
> - If True, it will download the picture and show the name of the downloaded file without displaying a picture.

> **markdown_name : bool, default False**
> - If True, display only a string with a file `file_name` inside `![SegmentLocal](file_name.file_format)` string.
It can be paste then, into markdown in for example **Jupyter Notebook**. When executed, 
it will display the picture inside markdown's cell.

> **Returns: image file and image object displayed**

