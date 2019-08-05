for file in * ; do      # or *.jpg, or x*.jpg, or whatever
        mv $file ${file^^}
done
