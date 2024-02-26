Desarrollo del Proyecto:
El desarrollo del proyecto se dividió en varias etapas:

Web Scraping: Se utilizó la biblioteca Selenium para extraer información relevante de las páginas web de Promptior, como los servicios ofrecidos y datos sobre la empresa.

Procesamiento del Lenguaje Natural (NLP): Se utilizó la biblioteca Langchain para construir un modelo de procesamiento del lenguaje natural capaz de generar respuestas automáticas basadas en las preguntas formuladas por los usuarios.

Aplicacion Web: Se creo una aplicacion Flask para proveer una interfaz de usuario sencilla con el endpoint para conectarme a la api de openAi.

Contenerización: La aplicación Flask y todas sus dependencias se contenerizaron utilizando Docker para facilitar su despliegue y ejecución en diferentes entornos.

Implementación en AWS: Se utilizó AWS Copilot para implementar y gestionar la infraestructura necesaria en AWS, incluyendo la configuración del clúster de contenedores, el balanceador de carga y otros recursos.

Uno de los desafíos clave fue aprender a usar Langchain para el procesamiento del lenguaje natural. Como era nuevo en esta biblioteca, tuve que sumergirme en la documentación, hacer un curso en Udemy y jugar bastante con ChatGPT para entender cómo encajaba todo en el proyecto del chatbot.

Además, lidiar con AWS Copilot para desplegar la aplicación fue otro desafío. Aunque ya tenía experiencia con AWS, nunca antes había usado Copilot, ni ECS. Así que, tuve que dedicar tiempo a aprender cómo funcionaba y cómo configurarlo para que la aplicación se desplegara sin problemas. Fue un poco como explorar un nuevo territorio, pero al final, logré tener la aplicación funcionando en la nube de AWS de manera eficiente.