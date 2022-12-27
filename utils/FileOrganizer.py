import os
import shutil
import filecmp
import glob

# from dotenv import load_dotenv
# load_dotenv()

# code by Leo
# inspired by this link: https://www.youtube.com/watch?v=KBjBPQExJLw&t=8s
class FileUtils:
    @staticmethod
    def organizeFilesIntoFolders(path: str, extensionsToSkip = [], onlyTargetTheseExtensions = []):
        files = os.listdir(path)
        if not files:
            print('this path has no files')
            return
        for file in files:
            # skip these extensions
            for ext in extensionsToSkip:
                if file.endswith(ext):
                    continue
            # only process these extensions
            for ext in onlyTargetTheseExtensions:
                if not file.endswith(ext):
                    continue
            # name of the file followed by .[ext]
            filename, ext = os.path.splitext(file)
            # print(file)
            ext = ext[1:]  # remove the leading period
            # print(filename, ext)
            currentFilePath = f'{path}/{file}'
            destinationFilePath = f'{path}/{ext}/{file}'

            # we need to create that folder first and then move it inside
            if not os.path.exists(f'{path}/{ext}'):
                print(
                    f'{path}/{ext} does not exist, so making a directory for it now')
                os.makedirs(f'{path}/{ext}')
            shutil.move(currentFilePath, destinationFilePath)


    @staticmethod
    def copyOverFile(sourceFile, destinationFile):
        '''
        compare the files to see if they're identical.
        If they are then don't copy overwrite to destinationPath.
        Otherwise overwrite
        '''
        # check that both files exist
        if not os.path.exists(sourceFile):
            print('source file does not exist')
            return
        if os.path.exists(destinationFile):
            # check that both files are the same
            if filecmp.cmp(sourceFile, destinationFile):
                print('files are the same')
                return

        print('overwriting destination file with the source')
        # overwrite contents of destinationFile with those of the source
        with open(sourceFile) as sf:
            contents = sf.readlines()
            with open(destinationFile, 'w') as df:
                df.writelines(contents)

    @staticmethod
    def copyOverFolder(sourceFolder, destinationFolder):
        # check that source file exist
        if not os.path.exists(sourceFolder):
            return
        # create destination folder if it doesn't exist already
        if not os.path.exists(destinationFolder):
            shutil.copytree(sourceFolder, os.path.basename(destinationFolder))

        # recursively check and compare all files in the source folder
        # maybe try filecmp.dircmp ?
        pass








#if os.getenv('PATH_TO_ORGANIZE') and os.path.exists(os.getenv('PATH_TO_ORGANIZE')):
#    FileUtils.organizeFilesIntoFolders(os.getenv('PATH_TO_ORGANIZE'))
