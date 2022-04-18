import math

                              ## Units: V--> m/s , Q,S,d --> m, theta, phy--> degree, G--> m/s²
Q = 7.32
S = 2.44
G = 9.8



def Goal_or_Not():

	d = 30
	input_theta = 366
	theta = (input_theta * math.pi)/180
	input_phy= 30
	phy = (input_phy * math.pi)/180
	V_initial = 10
	result = "Unable to deduce!"

	if abs(math.tan(theta)) >= (0.5 * Q)/d:
		result = "Not a goal, outside the two posts"
		return result

	else:
	                            #### Phase 1 ####
		#V_x_1 = V_initial * acos(phy)
		#V_y_2 = V_initial * asin(phy) - (G * T)

		T = (V_initial * math.sin(phy)) / G                         # Calc time taken to reach highest point at phase 1
		S_x_1 = V_initial * math.cos(phy) * T                       # Then using time calc horizontal distace covered 
		S_y_1 = (V_initial * math.sin(phy) * T) - ((G * T * T)/2)   # Then calc the height at this time 

									 #### Phase 2 ####

		          #### we want to know the height of the ball (S_y_2) when it reaches the goal line (S_x_2) ####

		S_x_2 = d
		T_2 = (S_x_2) / (V_initial * math.cos(phy)) 
		S_y_2 = G * T_2 * T_2 * 0.5

		if S >= (S_y_2 - S_y_1):
			result = "Not goal, above the crossbar"
			return result
		else :
			result = "GOAAAAAAAAAAAAAAAAL!!!!"
			return result
 



print(Goal_or_Not())
