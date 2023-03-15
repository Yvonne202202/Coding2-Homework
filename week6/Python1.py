#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# In[2]:


# Load the os library
import os

# Load the request module
import urllib.request

# Import SSL which we need to setup for talking to the HTTPS server
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create a directory
try: 
    os.mkdir('img_align_celeba')

    # Now perform the following 100 times:
    for img_i in range(1, 101):

        # create a string using the current loop counter
        f = '000.%03d.png' % img_i

        # and get the url with that string appended the end
        url = 'https://s3.amazonaws.com/cadl/celeb-align/' + f

        # We'll print this out to the console so we can see how far we've gone
        print(url, end='\r')

        # And now download the url to a location inside our new directory
        urllib.request.urlretrieve(url, os.path.join('img_align_celeba', f))
except:
    #os.rm('img_align_celeba')
    print("You may need to delete the existing 'img_align_celeba' folder in your directory")


# In[3]:


files = os.listdir('img_align_celeba')# img.<tab>
import matplotlib.pyplot as plt
import numpy as np

print(os.path.join('img_align_celeba', files[0]))
plt.imread(os.path.join('img_align_celeba', files[0]))

files = [os.path.join('img_align_celeba', file_i)
 for file_i in os.listdir('img_align_celeba')
 if '.png' in file_i]

# There should be 100 files, with the last one being number 99

img1 = plt.imread(files[99])
img2 = plt.imread(files[50])
print(img1)
print(img2)


# In[4]:


# If nothing is drawn and you are using notebook, try uncommenting the next line:
#%matplotlib inline
plt.imshow(img1)


# In[5]:


plt.imshow(img2)


# In[6]:


img1.shape


# In[7]:


img2.shape


# In[8]:


plt.imshow(img1)


# In[9]:


plt.imshow(img2)


# In[10]:


plt.imshow(img1, cmap='gray')


# In[11]:


plt.imshow(img2, cmap=plt.cm.gray)


# In[12]:


plt.set_cmap('gray')
# or
plt.set_cmap(plt.cm.gray)
# or even
plt.gray()

plt.imshow(img1)


# In[13]:


fig, ax = plt.subplots(1, 2)


# In[14]:


fig, ax = plt.subplots(1, 2)
ax[0].imshow(img1)
ax[1].imshow(img2)


# In[15]:


img1_no_alpha = img1[0:628, 0:500, 0:3]
img1_no_alpha.shape


# In[16]:


img2_no_alpha = img2[0:628, 0:500, 0:3]
img2_no_alpha.shape


# In[17]:


img1_no_alpha = img1[:, :, :2]


# In[18]:


img2_no_alpha = img2[:, :, :-1]


# In[19]:


np.mean(img1_no_alpha)


# In[20]:


img1_gray = np.mean(img1_no_alpha, axis=2)
img1_gray.shape


# In[21]:


img2_gray = np.mean(img2_no_alpha, axis=2)
plt.imshow(img2_gray)


# In[22]:


#calculate the difference between the two images
diff = img1_gray - img2_gray
plt.imshow(diff)


# In[23]:


(diff.min(), diff.max())


# In[24]:


diff_squared = diff**2
plt.imshow(diff_squared)


# In[25]:


diff_thresholded = diff_squared > 0.05
plt.imshow(diff_thresholded)


# In[26]:


diff_thresholded


# In[27]:


xdim, ydim = img1_gray.shape
img1_gray_3d = np.reshape(img1_gray, (xdim, ydim, 1))
img1_gray_3d.shape


# In[28]:


img1_gray_3d = img1_gray[:, :, None]
img1_gray_3d.shape


# In[29]:


diff_rgb = np.tile(img1_gray_3d, (1, 1, 3))
diff_rgb.shape


# In[30]:


red = [1, 0, 0]
diff_rgb[diff_thresholded, :] = red
plt.imshow(diff_rgb)


# In[31]:


fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.imshow(img1)
ax2.imshow(img2)
ax3.imshow(diff_rgb)


# In[32]:


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))
ax1.imshow(img1)
ax2.imshow(img2)
ax3.imshow(diff_rgb)


# In[33]:


imgs = [plt.imread(files[file_i])
        for file_i in range(100)]

#imgs = utils.get_celeb_imgs() # nope nope nope


# In[34]:


plt.imshow(imgs[59])


# In[35]:


data = np.array(imgs) # make 'data' = our numpy array
data.shape
print(data.shape)


# In[36]:


mean_img = np.mean(data, axis=0) # This is the mean of the 'batch' channel
plt.imshow(mean_img)
print("look at this average animals")


# In[37]:


mean_img


# In[38]:


std_img = np.std(data, axis=0)
plt.imshow(std_img)
print("This is the standard deviation - the variance of the mean")


# In[39]:


mean_img


# In[40]:


plt.imshow(np.mean(std_img, axis=2)) # Mean of all colour channels
print("Mean of all colour channels")


# In[41]:


flattened = data.ravel()
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html
print(data[:1])
print(flattened[:10])


# In[42]:


plt.hist(flattened.ravel(), 256)


# In[43]:


bins = 50
fig, axs = plt.subplots(1, 3, figsize=(10,8), sharey=True, sharex=True)
axs[0].hist((data[0]).ravel(), bins)
axs[0].set_title('img distribution')
axs[1].hist((mean_img).ravel(), bins)
axs[1].set_title('mean distribution')
axs[2].hist((data[0] - mean_img).ravel(), bins)
axs[2].set_title('(img - mean) distribution')


# In[44]:


fig, axs = plt.subplots(1, 3, figsize=(10,8), sharey=True, sharex=True)
axs[0].hist((data[0] - mean_img).ravel(), bins)
axs[0].set_title('(img - mean) distribution')
axs[1].hist((std_img).ravel(), bins)
axs[1].set_title('std deviation distribution')
axs[2].hist(((data[0] - mean_img) / std_img).ravel(), bins)
axs[2].set_title('((img - mean) / std_dev) distribution')


# In[45]:


axs[2].set_xlim([-100, 100])
axs[2].set_xlim([-50, 50])
axs[2].set_xlim([-20, 20])
axs[2].set_xlim([-5, 5])
axs[2].set_xlim([-1, 1])


# In[46]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# In[47]:


x = np.linspace(-3.0, 3.0, 100)

# Immediately, the result is given to us.  An array of 100 numbers equally spaced from -3.0 to 3.0.
print(x)

# We know from numpy arrays that they have a `shape`, in this case a 1-dimensional array of 100 values
print(x.shape)

# and a `dtype`, in this case float64, or 64 bit floating point values.
print(x.dtype)


# In[48]:


x = tf.linspace(-3.0, 3.0, 100)
print(x)


# In[49]:


g = tf.get_default_graph()


# In[50]:


g.get_tensor_by_name('linspace/Slice' + ':0')


# In[51]:


# We're first going to create a session:
sess = tf.Session()

# Now we tell our session to compute anything we've created in the tensorflow graph.
computed_x = sess.run(x)
print(computed_x)

# Alternatively, we could tell the previous Tensor to evaluate itself using this session:
computed_x = x.eval(session=sess)
print(computed_x)

# We can close the session after we're done like so:
sess.close()


# In[52]:


sess = tf.Session(graph=g)
sess.close()


# In[53]:


g2 = tf.Graph()


# In[54]:


sess = tf.InteractiveSession()
x.eval()


# In[55]:


# We can find out the shape of a tensor like so:
print(x.get_shape())

# %% Or in a more friendly format
print(x.get_shape().as_list())


# In[56]:


# The 1 dimensional gaussian takes two parameters, the mean value, and the standard deviation, which is commonly denoted by the name sigma.
mean = 0.0
sigma = 1.0

# Don't worry about trying to learn or remember this formula.  I always have to refer to textbooks or check online for the exact formula.
z = (tf.exp(tf.negative(tf.pow(x - mean, 1.0) /
                   (3.0 * tf.pow(sigma, 2.0)))) *
     (1.0 / (sigma * tf.sqrt(2.0 * 3.1415))))


# In[57]:


res = z.eval()
plt.plot(res)
# if nothing is drawn, and you are using ipython notebook, uncomment the next two lines:
#%matplotlib inline
#plt.plot(res)


# In[58]:


# Let's store the number of values in our Gaussian curve.
ksize = z.get_shape().as_list()[0]

# Let's multiply the two to get a 2d gaussian
z_2d = tf.matmul(tf.reshape(z, [ksize, 1]), tf.reshape(z, [1, ksize]))

# Execute the graph
plt.imshow(z_2d.eval())


# In[ ]:





# In[ ]:





# In[ ]:




