alist=input()
res=len(alist)-alist.count("c=")-alist.count("d-")-alist.count("c-")-alist.count("lj")-alist.count("nj")-(2*alist.count("dz="))-(alist.count("z=")-alist.count("dz="))-alist.count("s=")
print(res)

