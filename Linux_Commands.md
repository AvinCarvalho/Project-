# Linux Command Cheat Sheet

pwd                       (Print current working directory)  
ls                        (List files/folders)  
ls -l                     (List detailed info: permissions, owner, size, etc.)  
ls -a                     (Include hidden files)  

cd                        (Change directory)  
cd ..                     (Move up one directory)  
cd ~                      (Go to home directory)  

mkdir folder_name          (Create new directory)  
touch file_name            (Create empty file or update timestamp)  

cat file_name              (Display file content)  
echo "text" > file_name    (Write content to file, overwrite)  
echo "text" >> file_name   (Append content to file)  

rm file_name               (Remove file)  
rm -r folder_name          (Remove directory recursively)  
rmdir folder_name          (Remove empty directory)  

chmod u+x file_name        (Add execute permission for user)  
chmod g-w file_name        (Remove write permission for group)  
chmod o+w file_name        (Add write permission for others)  
chmod 764 file_name        (Numeric permissions: user=rwx, group=rw, others=r)  

grep "pattern" file_name   (Search text in a file)  
find /path -type f -name "file_name"  (Search file in directory tree)  

head file_name             (Show first 10 lines of file)  
head -n 5 file_name        (Show first 5 lines of file)  
tail file_name             (Show last 10 lines of file)  
tail -n 5 file_name        (Show last 5 lines of file)  
tail -f file_name          (Follow live updates of file)  

diff file1 file2           (Compare two files line by line)  
sed -i 's/old_text/new_text/' file_name   (Stream editor: replace text in file)  

tar -cvf archive_name.tar folder_name   (Create a tar archive)  
tar -xvf archive_name.tar              (Extract tar archive)
