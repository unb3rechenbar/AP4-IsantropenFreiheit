# Define the numerical solution to the Lorentz attractor DGL System
# with the Euler method
# and plot the result

using Plots
gr()

# Define the DGL System
function f(x,y,z)
    return 10*(y-x), x*(28-z)-y, x*y-8/3*z
end

# Define the Euler method
function euler(f, x0, y0, z0, h, n)
    x = zeros(n)
    y = zeros(n)
    z = zeros(n)
    x[1] = x0
    y[1] = y0
    z[1] = z0
    for i in 1:n-1
        x[i+1] = x[i] + h*f(x[i], y[i], z[i])[1]
        y[i+1] = y[i] + h*f(x[i], y[i], z[i])[2]
        z[i+1] = z[i] + h*f(x[i], y[i], z[i])[3]
    end
    return x, y, z
end

# Define the parameters
x0 = 1.0
y0 = 1.0
z0 = 1.0
h = 0.01
n = 10000

# Calculate the solution
x, y, z = euler(f, x0, y0, z0, h, n)


# Plot the solution
plt = plot(x, y, z, label = "Lorentz Attractor", title = "Lorentz Attractor", xlabel = "x", ylabel = "y", zlabel = "z")
gui(plt)

# Save the plot
savefig("Lorentz_Attractor.png")