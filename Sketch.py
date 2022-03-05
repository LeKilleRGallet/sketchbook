import matplotlib.pyplot as plt

years=[1950,1960,1970,1980,1990,1994,1998,2002,2006,2008,2012]
acres_mean=[213,297,374,426,461,478,460,425,372,295,213]

years_base_1950=[i-1950+1 for i in years]



a_vals=[]
b_vals=[]
c_vals=[]

def new_func(acres_mean, years_base_1950, i, j, k):
    c=((acres_mean[k])*(years_base_1950[i]**3)*(years_base_1950[j])+(acres_mean[k])*(years_base_1950[i]**2)*(years_base_1950[j]**2)+(acres_mean[j])*(years_base_1950[i]**2)*(years_base_1950[k]**2)-(years_base_1950[i])*(years_base_1950[j])*(years_base_1950[k]**2)*(acres_mean[i])-(2*years_base_1950[j]**2)*(years_base_1950[k]**2)*(acres_mean[i])-(acres_mean[j])*(years_base_1950[i]**3)*(years_base_1950[k])+(years_base_1950[i])*(years_base_1950[j]**2)*(years_base_1950[k])*(acres_mean[i]))/((years_base_1950[i]**2)*(years_base_1950[k]**2)-(years_base_1950[i])*(years_base_1950[j])*(years_base_1950[k]**2)-(2*years_base_1950[j]**2)*(years_base_1950[k]**2)-(years_base_1950[i]**3)*(years_base_1950[k])+(years_base_1950[i])*(years_base_1950[j]**2)*(years_base_1950[k])+(years_base_1950[i]**3)*(years_base_1950[j])+(years_base_1950[i]**2)*(years_base_1950[j]^2))
    return c

for i in range(10):
    for j in range(i+1,10):
        for k in range(j+1,10):
            c = new_func(acres_mean, years_base_1950, i, j, k)
            b=((years_base_1950[i]**2)*acres_mean[j]-(years_base_1950[i]**2)*c-(years_base_1950[j]**2)*(acres_mean[i])+(years_base_1950[j]**2)*c)/((years_base_1950[j]**2)*years_base_1950[i]+(years_base_1950[i]**2)*years_base_1950[j])
            a=(acres_mean[i]-c+years_base_1950[i]*b)/(years_base_1950[i]**2)
            a_vals.append(a)
            b_vals.append(b)
            c_vals.append(c)



c_mean=sum(c_vals)/len(c_vals)
b_mean=sum(b_vals)/len(b_vals)
a_mean=sum(a_vals)/len(a_vals)

print(f'y={round(a,2)}x^2+{round(b,2)}x+{round(c,2)}')

plt.scatter(years_base_1950,acres_mean)
plt.plot(years_base_1950, [a*i**2+b*i+c for i in years_base_1950])
plt.show()