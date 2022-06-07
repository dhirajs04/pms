create table if not exists users
(

    user_id       serial       not null,
    user_code     varchar(120) not null,
    username      varchar(120) not null,
    role          varchar(120) not null,
    web_token     varchar(255),
    is_web_logged boolean default false,
    mob_token     varchar(255),
    is_mob_logged boolean default false,
    is_verified   boolean default false,
    is_active     boolean default false,
    created_by    smallint     not null,
    created_at    timestamp    not null,
    updated_by    smallint,
    updated_at    timestamp,

    primary key (user_id)
);

create table if not exists profile
(
    profile_id  serial       not null,
    user_id     integer      not null,
    first_name  varchar(120) not null,
    last_name   varchar(120) not null,
    gender      varchar(7)   not null,
    dob         varchar(10),
    email       varchar(255),
    mobile_no   varchar(15),
    profile_img varchar(255),
    created_by  smallint     not null,
    created_at  timestamp    not null,
    updated_by  smallint,
    updated_at  timestamp,

    primary key (profile_id);

);