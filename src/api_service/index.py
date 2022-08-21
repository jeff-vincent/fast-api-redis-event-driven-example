index_view = """
<!DOCTYPE html>
<html>
   <head>
      <title>Distance to Velocity</title>
   </head>
   <body style="background-color:grey;">
        <h1 style="color: #585972; margin: 15px;">Distance to Velocity</h1>
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/distance" method="post">
            <p><input type=text name=email placeholder=" your email...">
            <p><input type=text name=lat placeholder=" your latitude...">
            <p><input type=text name=long placeholder=" your longitude...">
            <p><input type=submit value="Get distance">
        </form>
        </div>
    </body>
</html>
"""