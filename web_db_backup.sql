PGDMP      	            
    {            web_db    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    139992    web_db    DATABASE     �   CREATE DATABASE web_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1250';
    DROP DATABASE web_db;
                postgres    false            �            1259    139994    transform_data    TABLE     �   CREATE TABLE public.transform_data (
    id integer NOT NULL,
    input_1 real,
    input_2 real,
    input_3 real,
    output_1 real,
    output_2 real,
    output_3 real,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
 "   DROP TABLE public.transform_data;
       public         heap    postgres    false            �            1259    139993    your_table_name_id_seq    SEQUENCE     �   CREATE SEQUENCE public.your_table_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.your_table_name_id_seq;
       public          postgres    false    216            �           0    0    your_table_name_id_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE public.your_table_name_id_seq OWNED BY public.transform_data.id;
          public          postgres    false    215            P           2604    139997    transform_data id    DEFAULT     w   ALTER TABLE ONLY public.transform_data ALTER COLUMN id SET DEFAULT nextval('public.your_table_name_id_seq'::regclass);
 @   ALTER TABLE public.transform_data ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �          0    139994    transform_data 
   TABLE DATA           q   COPY public.transform_data (id, input_1, input_2, input_3, output_1, output_2, output_3, created_at) FROM stdin;
    public          postgres    false    216   �       �           0    0    your_table_name_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.your_table_name_id_seq', 9, true);
          public          postgres    false    215            S           2606    140000 #   transform_data your_table_name_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.transform_data
    ADD CONSTRAINT your_table_name_pkey PRIMARY KEY (id);
 M   ALTER TABLE ONLY public.transform_data DROP CONSTRAINT your_table_name_pkey;
       public            postgres    false    216            �   G   x�]��� ��QE�N@�%���y�.8�D��#��qX�K�v�l�e3�7���TmQ^��%X     