CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Users ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'profile_image_url', 'bio', 'created_on') VALUES (27, 'Rob', 'Zombie', 'Zomboy', 'robo@mail.com', 'm00n', 'https://images.unsplash.com/photo-1572527561845-bf58d45376bc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8em9tYmllfGVufDB8fDB8fA%3D%3D&w=1000&q=80', 'More human than human', 3);
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Mood');
INSERT INTO Categories ('label') VALUES ('Intention');
INSERT INTO Categories ('label') VALUES ('Subject');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Posts ('category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('1', 'Mood', '11.04.2022', 'https://static.vecteezy.com/system/resources/previews/006/828/449/original/face-emoji-expressing-a-happy-mood-free-vector.jpg', 'I am happ because this shit works', 1)
INSERT INTO Posts ('category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('2', 'Mood', '11.02.2022', 'https://images.unsplash.com/photo-1531260796528-ae45a644fb20?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8c2FkJTIwbW9vZHxlbnwwfHwwfHw%3D&w=1000&q=80', 'I was a pissy dude after the car wreck', 1)
INSERT INTO Posts ('category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('2', 'Mood', '11.06.2022', 'https://production.listennotes.com/podcasts/bear-psychology-podcast-dr-anna-baranowsky-2WFOMyLS8tl-zluxvHOr3Sb.300x300.jpg', 'I am feeling dickish today', 1)
INSERT INTO Posts ('category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('4', 'Life is Python', '11.07.2022', 'https://bigthink.com/wp-content/uploads/2022/07/AdobeStock_379164614.jpeg?w=480&h=270&crop=1', 'What a stinking hole of lies', 1);

INSERT INTO PostReactions ('id', 'reaction_id', 'user_id', 'post_id') VALUES (3, 1, 1, 2);
INSERT INTO PostReactions ('id', 'reaction_id', 'user_id', 'post_id') VALUES (4, 2, 2, 5);
INSERT INTO Reactions ('id', 'label', 'image_url') VALUES ('1', 'Big Grin', '????')
INSERT INTO Reactions ('id', 'label', 'image_url') VALUES ('2', 'Smile', '????')

SELECT
    s.id,
    s.follower_id,
    s.created_on,
    u.id author_id
FROM Subscriptions s
LEFT JOIN Users u
    ON  u.id = s.author_id

SELECT
    p.title,
    u.first_name first_name,
    u.last_name last_name
FROM Posts p
LEFT JOIN Users u
    ON u.id = p.user_id

SELECT
    p.title,
    c.id category_id
FROM Categories c
LEFT JOIN Posts p
    ON p.id = p.category_id
    WHERE label = 'Jo Mama'

SELECT *
FROM Users u

INSERT INTO Comments ('author_id', 'post_id', 'content') Values (1, 23,'If I were a turtle')

INSERT INTO Comments ('author_id', 'post_id', 'content') Values (2, 24,'If I were a beeeeerrrr')

INSERT INTO Comments ('author_id', 'post_id', 'content') Values (3, 25,'I am a whiskey')

INSERT INTO Users ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'bio', 'created_on') VALUES (91, 'Rob', 'Thomas', 'Matchbox21', 'realworld@mail.com', 'm00n', 'The note she wrote', '11.11.2011');
INSERT INTO Users ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'bio', 'created_on') VALUES (92, 'Frank', 'Ocean', 'Hazbeen', 'channelgreen@mail.com', 'm00n', 'We used to have things in common', '12.12.2012');
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') Values (1, 91,'3.3.2013');
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') Values (1, 92,'4.4.2014');
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('91', '1', 'Rightwards', '11.04.2022', 'https://static.vecteezy.com/system/resources/previews/006/828/449/original/face-emoji-expressing-a-happy-mood-free-vector.jpg', 'Its a direction people like', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('91', '1', 'Leftwards', '11.04.2022', 'https://static.vecteezy.com/system/resources/previews/006/828/449/original/face-emoji-expressing-a-happy-mood-free-vector.jpg', 'Its a direction people are suspicious of', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES ('92', '1', 'Upwards', '11.04.2022', 'https://static.vecteezy.com/system/resources/previews/006/828/449/original/face-emoji-expressing-a-happy-mood-free-vector.jpg', 'Its the direction to Gods front porch', 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES ('7', '1')
INSERT INTO PostTags ('post_id', 'tag_id') VALUES ('7', '3')

        SELECT

            pt.post_id,
            pt.tag_id,
            t.id,
            t.label,
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM PostTags pt
        LEFT JOIN Tags t
            ON pt.tag_id = t.id
        LEFT JOIN Posts p
            ON pt.post_id = p.id
        WHERE t.label = 'stinky'

        SELECT
            c.id,
            c.label,
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Categories c
        LEFT JOIN Posts p
            ON c.id = p.category_id
        WHERE c.label = 'Mood'

       SELECT
            u.first_name,
            u.last_name,
            u.email,
            u.username
        FROM Users u
        ORDER BY username ASC

UPDATE Users
SET active = 1
WHERE username = 'dadbod'

UPDATE Users
SET profile_image_url = 'https://m.media-amazon.com/images/I/51XVZYDA0ZL._AC_SY580_.jpg'
WHERE username = 'usaxary25'

UPDATE Users
SET profile_image_url = 'https://i.pinimg.com/736x/a5/c1/f9/a5c1f9dbaffe6faff24eaff365b2d6dc--funny-poses.jpg'
WHERE username = 'sdsdf'

UPDATE Users
SET active = 1
WHERE username = 'Zomboy'

        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.username,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content
        FROM Users u
        LEFT JOIN Posts p
            ON u.id = p.user_id
        WHERE u.username = 'dadbod'

UPDATE Posts
SET user_id = 27
WHERE title = 'Leftwards'
