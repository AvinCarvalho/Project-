# Linux Quick Command Cheat Sheet (WSL)

pwd [pwd] – Print current working directory  
ls [ls] – List files/folders  
ls -l [ls -l] – Detailed info (permissions, owner, size)  
ls -a [ls -a] – Include hidden files  

cd [cd] – Change directory  
cd .. [cd ..] – Move up one directory  
cd ~ [cd ~] – Go to home directory  

mkdir [mkdir folder_name] – Make new directory  
touch [touch file_name] – Create empty file or update timestamp  

cat [cat file_name] – Display file content  
echo "text" > file_name [echo "text" > file_name] – Overwrite content  
echo "text" >> file_name [echo "text" >> file_name] – Append content  

rm [rm file_name] – Remove file  
rm -r [rm -r folder_name] – Remove directory recursively  
rmdir [rmdir folder_name] – Remove empty directory  

chmod u+x file_name [chmod u+x file_name] – Add execute for user  
chmod g-w file_name [chmod g-w file_name] – Remove write for group  
chmod 764 file_name [chmod 764 file_name] – Numeric permissions  

grep "pattern" file_name [grep "pattern" file_name] – Search text in file  
find /path -type f -name "file_name" [find /path -type f -name "file_name"] – Find file  

head file_name [head file_name] – First 10 lines  
head -n 5 file_name [head -n 5 file_name] – First 5 lines  
tail file_name [tail file_name] – Last 10 lines  
tail -n 5 file_name [tail -n 5 file_name] – Last 5 lines  
tail -f file_name [tail -f file_name] – Follow live updates  

diff file1 file2 [diff file1 file2] – Compare two files line by line  
sed -i 's/old_text/new_text/' file_name [sed -i 's/old_text/new_text/' file_name] – Replace text in file
