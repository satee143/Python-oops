from pathlib import Path

ctl_dir = Path('/proc').glob('[0-9]*/status')
clt_id = [(r_st.parent.name,r_st.read_text().splitlines()[0]) for r_st in ctl_dir] 
for pid, pname in clt_id:
	print("{}  {}".format(pid, pname).replace("Name:",''))