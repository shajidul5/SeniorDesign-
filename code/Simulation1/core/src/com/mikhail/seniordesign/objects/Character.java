package com.mikhail.seniordesign.objects;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Circle;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;

/**
 * Created by mikhail on 12/6/17.
 */
public class Character {

    public static final int RADIUS = 10;
    public static int VEL = 120;
    private Circle bounds;
    private final Texture texture;

    static Texture colLeftTexture;
    static Texture colRightTexture;

    static {
        Pixmap px = new Pixmap(5, 5, Pixmap.Format.RGB565);
        px.setColor(Color.BLUE);
        px.fill();
        colLeftTexture = new Texture(px);
        px.setColor(Color.YELLOW);
        px.fill();
        colRightTexture = new Texture(px);
        px.dispose();
    }

    private static final Circle INIT_BOUNDS = new Circle(30, 30, RADIUS);

    private Array<Collision> collisions = new Array<Collision>();
    private final Vector2 pull;


    public Character() {
        bounds = new Circle(INIT_BOUNDS);
        Pixmap px = new Pixmap(RADIUS, RADIUS, Pixmap.Format.RGBA8888);
        px.setColor(Color.GREEN);
        px.fillCircle(RADIUS / 2, RADIUS / 2, RADIUS);
        texture = new Texture(px);
        px.dispose();

        pull = new Vector2(250, 30);

    }

    public void draw(SpriteBatch batch) {
        batch.draw(texture, bounds.x, bounds.y);
        for (Collision col : collisions) {
            Vector2 pt = col.point;
            batch.draw(col.goRight ? colRightTexture : colLeftTexture, pt.x - 2, pt.y - 2);
        }
    }

    private int angle = 0;
    private int lastColPoint = 0;

    public void act(float dTime) {

        Vector2 currentPos = new Vector2(bounds.x, bounds.y);

        boolean move = true;

        Vector2 nextPos;
        do {
            move = true;
            nextPos = new Vector2(currentPos);
            Vector2 motion = new Vector2();

            motion.setToRandomDirection();

            motion = motion.setLength(VEL * dTime);
            System.out.println("motion="+ motion);

            motion = motion.setAngle(angle);
            System.out.println("motion="+ motion);

            nextPos.add(motion);

            for (int i = 0; i < collisions.size; i++) {
                Collision collision = collisions.get(i);
                Vector2 collisionPoint = collision.point;
                if (nextPos.dst(collisionPoint) < 2*RADIUS) {
                    /*if(i < lastColPoint){
                        collisions.get(collisions.size-3).goRight = !collisions.get(collisions.size-3).goRight;
                        collisions.removeRange(collisions.size-2, collisions.size-1);
                        lastColPoint = collisions.size-3;
                    }*/

                    angle = (angle + (collision.goRight ? -90 : 90) + 360) % 360;
                    move = false;
                    lastColPoint++;
                    break;

                }
            }

        }while(!move);
        System.out.println("nextPos="+nextPos);
        bounds.x = nextPos.x;
        bounds.y = nextPos.y;

    }

    public void collision() {
        Collision newCollision = new Collision(new Vector2(bounds.x, bounds.y), false);

        if(collisions.size == 0){
            collisions.add(newCollision);
            bounds.set(INIT_BOUNDS);
            lastColPoint = 0;
            angle = 0;
            return;
        }

        Collision lastCollision = collisions.get(collisions.size-1);

        if(newCollision.point.dst(lastCollision.point) < 70) {
            lastCollision.goRight = !lastCollision.goRight;
        }else{

        collisions.add(newCollision);


        }

        bounds.set(INIT_BOUNDS);
        lastColPoint = 0;
        angle = 0;

    }

    public void checkCollision(Maze maze) {
        for (Wall wall : maze.walls) {
            if (wall.bounds.contains(bounds.x, bounds.y)) {
                collision();
                break;
            }
        }
    }

}
