# INTEGRACIÓN DE SISTEMAS EMPRESARIALES AVANZADO 
# LABORATORIO N° 07: MÓDULO PUNTO DE VENTA

# Alumno: Carlos Enrique Alvarez Iquiapaza

2.2. La interfaz de venta es relativamente fácil de utilizar. Automáticamente incluirá todos los productos
que ya hayamos registrado en el sistema
![image1](./images/Punto2_2.PNG)


2.3. Podemos incluso elegir entre los clientes que tengamos ya registrados con hacer click en Cliente.
Agregue un GIF de cómo se vería la creación de un cliente nuevo y su selección.
![image2](./images/Punto2_3.gif)

2.4. Así mismo, al dar click en el botón Pago, encontraremos una interfaz sencilla, donde elegiremos el
medio de pago y demás condiciones. Por ahora nos aparecerá solamente con Efectivo
(configuraremos más adelante otros medios como VISA o MASTERCARD)
![image3](./images/Punto2_4.PNG)


2.5. Ingresado ya el medio de pago, de click en validar, aparecerá la impresión del ticket o comprobante
de pago.
![image4](./images/Punto2_5.PNG)

2.6. Vamos a dar click una vez en Cerrar y luego otra vez en Confirmar (esto evita que se cierre de manera
accidental el punto de venta). Si nos dirigimos al listado de Sesiones y vemos la sesión actual veremos
el total en efectivo de las transacciones del Punto de Venta. De esta manera tendremos un control de
cierre de turno. Proceda a cerrar y validar esta sesión para iniciar otra con una nueva configuración.
![image5](./images/Punto2_6.PNG)

3.2. Habilite la opción de Control de Precios.
![image6](./images/Punto3_2.PNG)

3.3. Intente iniciar una nueva sesión de venta. Verá que ahora no lo redirige directamente al Punto de
Venta, sino que aparece una ventana previa. Aquí podrá configurar un Balance de Apertura.
![image7](./images/Punto3_3.PNG)

![image8](./images/Punto3_3_1.PNG)

3.4. Ahora sí, iniciaremos el Punto de Venta. Haga una venta que tenga dos medios de pago. Verá que
Odoo permite pagar de distintas formas, con efectivo, con efectivo y otros medios combinado,
solamente un medio bancarizado sin efectivo, etc. Añada imágenes de dichas ventas y comente las
combinaciones que logró.
![image9](./images/Punto3_4.PNG)

3.7. En la parte superior del Punto de Venta (ingrese de nuevo o refresque la ventana con F5) haga click
en el nombre del usuario (Administrador o el nombre que le haya colocado) y vera una ventana de
selección de usuario. Adjunte dicha imagen.
Ahora, elija al usuario cajero y vea como se bloquea la opción Precio. Solamente un administrador
puede modificar precios con la opción habilitada Control de precios
![image10](./images/Punto3_7.PNG)

3.8. Intente acceder como Administrador. Verá que le solicita una contraseña, que justamente será la
misma que colocamos en pasos anteriores. Verifique que ahora se habilite el botón de modificar
precios.
![image11](./images/Punto3_8.PNG)

4.2. Proceda a crear dos categorías:
Frutas
Útiles Escolares.
![image12](./images/Punto4_2.PNG)

4.3. Vamos a editar un producto. En la pestaña Ventas, aparecerá la opción Punto de Venta. Dentro de
ella, selecciona una de las dos categorías creadas. Repita esto con al menos 10 productos.
![image13](./images/Punto4_3.PNG)

4.4. Refresque el Punto de Venta y vea como ahora se agregan las categorías creadas.
![image14](./images/Punto4_4.PNG)

5.1. Crearemos un nuevo punto de venta llamado Cafetería
![image15](./images/Punto5_1.PNG)

5.4. Ahora sí, ingrese al nuevo punto de venta. Verá las opciones de los pisos creados. Hagamos click en
el lápiz ubicado a la derecha. Este nos servirá para dibujar las mesas del restaurante. Proceda a
dibujarlas.
![image16](./images/Punto5_4.PNG)

5.5. Para hacer un pedido, debemos estar fuera del modo de edición y hacer click en una mesa.
![image17](./images/Punto5_5.gif)

5.6. Tenemos un nuevo botón, que sirve para añadir notas a los pedidos. Así se le pueden añadir
personalizaciones al pedido, como por ejemplo añadir mayonesa o preparar sin sal.
![image18](./images/Punto5_6.PNG)

5.7. También tenemos un botón de Transferir que sirve para mover el pedido de una mesa a otra. Añada
un GIF mostrando esta funcionalidad.
![image19](./images/Punto5_7.gif)

5.9. Ahora tenemos el botón Recibo, que sirve para imprimir la pre-cuenta (o llamada también comanda).
Esto es útil para cuando los clientes piden el total para saber cuánto han consumido.
![image20](./images/Punto5_9.PNG)

![image21](./images/Punto5_9_1.PNG)


# Conlusiones

Fue necesario instalar el modulo de venta, para establecer que tarjetas son permitidas en el establecimiento y hacer como una simulacion de un local.

Gracias al punto de venta nosotros como dueños de negocio o desarrolladores podemos maquetar o diseñar la forma de como es nuestro local en simulador de punto de venta.

Fue necesario la resolucion de laboratorios anteriores para la compresiony realizacion de este

Configuramos nuestro administrador agregando un pin para que cuando queramos entrar como admin para hacer una venta este nos pida el mismo pin como forma de seguridad 
