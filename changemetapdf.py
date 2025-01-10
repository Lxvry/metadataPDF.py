import fitz

#Enter the name of the pdf file to change the metadata
doc = fitz.open('pdf')

new_metadata = {
            'producer':'', //Here you can add the tags and content you want to modify
            'creator' : ''
        }

#Now we save everything, as a neww pdf file.
doc.set_metadata(new_metadata)
doc.save("document1_New.pdf")

doc.close()

