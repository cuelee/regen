import numpy 

def LS_z(betas, stders, cor):
	bes = list(map(float,betas))
	C = np.matrix(cor,dtype=float)
	stds_np = np.matrix(np.diag(list(map(float,stders))))

	V = stds_np.dot(C).dot(stds_np)
	Vinv = np.linalg.inv(V)
	ones = np.matrix(list(map(float,[1]*len(bes))))

	newv = 1 / (ones.dot(Vinv).dot(ones.transpose()))
	newx = np.matrix(ones).dot(Vinv).dot(np.matrix(bes).transpose()) / (ones.dot(Vinv).dot(ones.transpose()))
	newstd = np.sqrt(newv)
	newz = newx/newstd
	return(newz) 
