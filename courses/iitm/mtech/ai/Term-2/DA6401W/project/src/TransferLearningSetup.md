Import libraries:

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
```

Load CIFAR‑10 Dataset
```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalize pixel values
x_train, x_test = x_train / 255.0, x_test / 255.0
```

Resize Images to Match Pretrained Model Input
Most pretrained models expect 224×224 input (ImageNet size):
```
python
x_train_resized = tf.image.resize(x_train, (224, 224))
x_test_resized = tf.image.resize(x_test, (224, 224)) 
```

Load Pretrained Model (Feature Extractor)
```
python
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))

# Freeze base model layers
base_model.trainable = False
```

Add Custom Classification Head
```
python
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')  # CIFAR-10 has 10 classes
])
```

Compile Model
```
python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Train Model
```
python
history = model.fit(x_train_resized, y_train,
                    epochs=5,
                    validation_data=(x_test_resized, y_test))
```

Fine‑Tuning (Optional)
Unfreeze deeper layers for better accuracy:
```
python
base_model.trainable = True
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),  # smaller LR
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history_ft = model.fit(x_train_resized, y_train,
                       epochs=3,
                       validation_data=(x_test_resized, y_test))
```