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
  created_at    timestamp    not null,
  updated_at    timestamp,

  primary key (user_id)
);

create table if not exists role
(
  role_id    serial       not null,
  name       varchar(150) not null unique,

  primary key (role_id)
);

create table if not exists role_permission
(
  role_permission_id serial       not null,
  role_id            smallint     not null,
  method             varchar(10)  not null,
  path_name          varchar(150) not null,
  read               boolean default false,
  write              boolean default false,
  update             boolean default false,
  delete             boolean default false,

  primary key (role_permission_id)

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