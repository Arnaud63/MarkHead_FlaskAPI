from deepface import DeepFace

picture="omar_sy.png"
facial_attributes = ['age', 'gender', 'race', 'emotion']

analyse = DeepFace.analyze(img_path = picture, actions = facial_attributes)
