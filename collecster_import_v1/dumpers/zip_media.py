#!/usr/bin/env python

import glob, os, shutil

def mkdir_conditional(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    elif not os.path.isdir(directory):
        raise Exception("'{}' is not a directory".format(directory))

def do_picture(path, entity_name, id_entry, destination):
        image_paths = []
        extensions = ("JPG", "jpg",)
        for ext in extensions:
            image_paths.extend(glob.glob(os.path.join(path, "*.{}".format(ext))))
        destination_pic_dir = os.path.join(destination, entity_name, id_entry, "pictures")
        mkdir_conditional(destination_pic_dir)
        for img in image_paths:
            shutil.copy2(img, os.path.join(destination_pic_dir, os.path.basename(img)))

        # sanity check
        all_files = [os.path.join(path, file) for file in os.listdir(path)
                                              if os.path.isfile(os.path.join(path, file)) and (file != ".DS_Store")]
        if set(all_files) != set(image_paths):
            raise Exception("{a} // {b}".format(a=all_files, b=image_paths))



def workit(images_path, bundle_images_path, destination):
    for bundle_id_entry in [entry for entry in os.listdir(bundle_images_path) if os.path.isdir(os.path.join(bundle_images_path, entry))]:
        bundle_path = os.path.join(bundle_images_path, bundle_id_entry)
        do_picture(bundle_path, "bundles", bundle_id_entry, destination)

    for occ_id_entry in [entry for entry in os.listdir(images_path) if os.path.isdir(os.path.join(images_path, entry))]:
        pk = int(occ_id_entry)
        occurrence_path = os.path.join(images_path, occ_id_entry)

        ## PICTURES
        do_picture(occurrence_path, "occurrences", occ_id_entry, destination)

        ## TAG
        tag_path = os.path.join(occurrence_path, "tag")
        files = [entry for entry in os.listdir(tag_path)
                    if os.path.splitext(entry)[1] == ".png"]
        if len(files)!=1 or not files[0].startswith("tag_"):
            raise Exception("{file}".format(files[0]))
        else:
            source_tag = os.path.join(tag_path, files[0])
            destination_dir = os.path.join(destination, "occurrences", occ_id_entry, "tags")
            mkdir_conditional(destination_dir)
            shutil.copy2(source_tag, os.path.join(destination_dir, "v1.png"))


workit("media/images/instances/", "media/images/bundles/", "export/media/advideogame/")
os.system("cd export && zip -r ../exported_media.zip media && cd -")
