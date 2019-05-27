import filecmp

a="/home/test/filecmp/dir1"
b="/home/test/filecmp/dir2"

dirobj=filecmp.dircmp(a,b,['test.py'])

print "-------------------report---------------------"
dirobj.report()
print "-------------report_partial_closure-----------"
dirobj.report_partial_closure()
print "-------------report_full_closure--------------"
dirobj.report_full_closure()

print "left_list:"+ str(dirobj.left_list)
print "right_list:"+ str(dirobj.right_list)
print "common:"+ str(dirobj.common)
print "left_only:"+ str(dirobj.left_only)
print "right_only:"+ str(dirobj.right_only)
print "common_dirs:"+ str(dirobj.common_dirs)
print "common_files:"+ str(dirobj.common_files)
print "common_funny:"+ str(dirobj.common_funny)
print "same_file:"+ str(dirobj.same_files)
print "diff_files:"+ str(dirobj.diff_files)
print "funny_files:"+ str(dirobj.funny_files)
