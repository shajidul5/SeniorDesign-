package com.mikhail.seniordesign.objects;

import com.badlogic.gdx.math.Vector2;

/**
 * Created by mikhail on 12/8/17.
 */
public class Collision {

    public final Vector2 point;
    public boolean goRight;

    public Collision(Vector2 point, boolean goRight) {
        this.point = point;
        this.goRight = goRight;
    }
}
