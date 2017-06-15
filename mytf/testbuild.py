import tensorflow as tf

matrix1 = tf.constant([[1,3]])
matrix2 = tf.constant([[4],[8]])

res = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
    with tf.device("/gpu:0"):
        print sess.run([res])
    with tf.device("/cpu:0"):
        print sess.run([res])
