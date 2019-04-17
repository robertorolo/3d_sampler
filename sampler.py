import numpy as np
import itertools
import random

def random_sampling(n_holes=10, nx=100, ny=50, nz=20, ox=0, oy=0, oz=0, sx=1, sy=1, sz=1, dir_i=[0,1,0,-1], dir_j=[0,0,1,0], step_k=[3,3,3,3], nz_buffer=[0]):
	top_slice = []
	
	for i, j in itertools.product(range(nx), range(ny)):
		top_slice.append([i,j,nz])

	random_sampling = np.random.randint(len(top_slice), size=n_holes)

	array = []

    #looping through every sampled node in top slice
	for hole_id, index in enumerate(random_sampling):
	    #appending first point on top slice
	    #sampled_df = sampled_df.append([row["i"], row["j"], row["k"]], ignore_index=True)
	    array.append([hole_id, top_slice[index][0], top_slice[index][1], top_slice[index][2]])
	    
	    #setting i, j position on top slice
	    i, j = top_slice[index][0], top_slice[index][1]
	    
	    #setting the hole direction
	    rn_dir = np.random.randint(len(dir_i))
	    k_step = step_k[rn_dir]
	    
	    buff = random.choice(nz_buffer)
	    nnz = nz + buff
	    
	    #looping slices down
	    for k in range(nz - k_step, nz-nnz, -k_step):
	        
	        #setting k
	        k = k
	        
	        #setting new i, j based on hole direction
	        i, j = i+dir_i[rn_dir], j+dir_j[rn_dir]
	        
	        #if not ox<=i<=nx or not oy<=j<=ny:
	        #    continue
	        
	        #appending to sampled df
	        #sampled_df = sampled_df.append([i, j, k], ignore_index=True)
	        array.append([hole_id, i, j, k])

	return array

def regular_sampling(nx=100, ny=50, nz=20, ox=0, oy=0, oz=0, sx=1, sy=1, sz=1, step_x=20, step_y=20, dir_i=[0], dir_j=[0], step_k=[3], nz_buffer=[0]):
	top_slice = []
	
	for i, j in itertools.product(range(int(ox),nx,step_x), range(int(oy),ny,step_y)):
		top_slice.append([i,j,nz])

	random_sampling = range(len(top_slice))

	array = []

	#looping through every sampled node in top slice
	for hole_id, index in enumerate(random_sampling):
		#appending first point on top slice
		#sampled_df = sampled_df.append([row["i"], row["j"], row["k"]], ignore_index=True)
		array.append([hole_id, top_slice[index][0], top_slice[index][1], top_slice[index][2]])

		#setting i, j position on top slice
		i, j = top_slice[index][0], top_slice[index][1]

		#setting the hole direction
		rn_dir = np.random.randint(len(dir_i))
		k_step = step_k[rn_dir]

		buff = random.choice(nz_buffer)
		nnz = nz + buff

		#looping slices down
		for k in range(nz - k_step, nz-nnz, -k_step):
		    
		    #setting k
		    k = k
		    
		    #setting new i, j based on hole direction
		    i, j = i+dir_i[rn_dir], j+dir_j[rn_dir]
		    
		    #if not ox<=i<=nx or not oy<=j<=ny:
		    #    continue
		    
		    #appending to sampled df
		    #sampled_df = sampled_df.append([i, j, k], ignore_index=True)
		    array.append([hole_id, i, j, k])

	return array